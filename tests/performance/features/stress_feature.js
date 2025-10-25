import http from 'k6/http';
import { sleep } from 'k6';

export const options = {
  executor: 'ramping-vus',
  startVUs: 0,
  stages: [
    { duration: '5s', target: 10 },
    { duration: '10s', target: 30 },
    { duration: '5s', target: 0 },
  ],
};

export function run() {
  http.get(`${__ENV.BITWARDEN_URL}/`);
  sleep(1);
}
