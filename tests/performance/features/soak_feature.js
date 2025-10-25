import http from 'k6/http';
import { sleep } from 'k6';

export const options = {
  executor: 'constant-arrival-rate',
  rate: 10,
  timeUnit: '1s',
  duration: '5s',
  preAllocatedVUs: 20,
};

export function run() {
  http.get(`${__ENV.BITWARDEN_URL}/`);
  sleep(1);
}