import { options as loadOpts, run as loadTest } from './load_feature.js';
import { options as soakOpts, run as soakTest } from './soak_feature.js';
import { options as spikeOpts, run as spikeTest } from './spike_feature.js';
import { options as stressOpts, run as stressTest } from './stress_feature.js';
import { options as customOpts, run as customTest } from './custom_feature.js';


export const options = {
  scenarios: {
    load_scenario: { ...loadOpts, exec: 'loadTest', startTime: '0s', },
    soak_scenario: { ...soakOpts, exec: 'soakTest', startTime: '10s', },
    spike_scenario: { ...spikeOpts, exec: 'spikeTest', startTime: '20s', },
    stress_scenario: { ...stressOpts, exec: 'stressTest', startTime: '40s', },
    custom_scenario: { ...customOpts, exec: 'customTest', startTime: '50s', }
  },
};

// Exporta las funciones para que K6 pueda encontrarlas
export { loadTest,soakTest,spikeTest,stressTest,customTest};