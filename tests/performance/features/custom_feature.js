import http from 'k6/http';
import { check, sleep } from 'k6';


// Configuración de la prueba
export const options = {
  executor: 'constant-vus',
  vus: 10,
  duration: '5s'
};

// Escenario principal
export function run() {
 
  const payload = {
    scope: 'api offline_access',
    client_id: 'web',
    deviceType: '9',
    deviceIdentifier: '8bf43c01-0331-4fad-a998-ef680e6ce661',
    deviceName: 'chrome',
    grant_type: 'password',
    username: __ENV.BITWARDEN_USER,
    password: __ENV.BITWARDEN_PASSWORD,
  };

  console.log('📦 Payload preparado:', JSON.stringify(payload, null, 2));

  const formBody = Object.entries(payload)
    .map(([key, value]) => `${encodeURIComponent(key)}=${encodeURIComponent(value)}`)
    .join('&');

  const res1 = http.post(`${__ENV.BITWARDEN_URL}/identity/connect/token`, formBody, { 
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
      'Bitwarden-Client-Name': 'web',
      'Bitwarden-Client-Version': '2025.10.0',
      'Device-Type': '9',
      'Origin': 'https://vault.bitwarden.com',
    },
  });
   
  console.log('🔎 Response status /connect/token:', res1.status);
  console.log('🔎 Response body /connect/token:', res1.body.substring(0, 300) + '...');

  check(res1, {
    'token request OK': (r) => r.status === 200,
    'access_token exists': (r) => r.json('access_token') !== undefined,
  });

  // Extraer el token del primer response
  const accessToken = res1.json('access_token');
  console.log('Access Token:', accessToken ? accessToken.substring(0, 40) + '...' : 'NO TOKEN');

  const res2 = http.get(`${__ENV.BITWARDEN_URL}/api/sync?excludeDomains=true`, {
    headers: { Authorization: `Bearer ${accessToken}` },
  });


  check(res2, {
    'sync request OK': (r) => r.status === 200,
    'sync response has data': (r) => r.body && r.body.length > 0,
    'sync time < 800ms': (r) => r.timings.duration < 800,
  });

  
  sleep(1); // simula espera de usuario
}