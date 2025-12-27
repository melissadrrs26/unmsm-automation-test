import http from 'k6/http';
import { sleep } from 'k6';

export const options = {
  executor: 'ramping-arrival-rate',
  preAllocatedVUs: 20,
  stages: [
    { duration: '5s', target: 100 },
    { duration: '5s', target: 10 },
  ],
};

export function run() {
  http.get(`${__ENV.BITWARDEN_URL}/`);
  sleep(0.5);
}