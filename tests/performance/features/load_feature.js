import http from 'k6/http';
import { sleep } from 'k6';

export const options = {
  executor: 'constant-vus',
  vus: 10,
  duration: '5s',
};

export function run() {
  http.get(`${__ENV.BITWARDEN_URL}/`);
  sleep(1);
}