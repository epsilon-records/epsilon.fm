import pino from 'pino';
import { logflarePinoVercel } from 'pino-logflare';
import { LOGFLARE_API_KEY, LOGFLARE_SOURCE_TOKEN } from '$env/static/private';

// Browser logs are going to: https://logflare.app/sources/32475
// Server logs are going to: https://logflare.app/sources/32465

const { stream, send } = logflarePinoVercel({
	apiKey: LOGFLARE_API_KEY,
	sourceToken: LOGFLARE_SOURCE_TOKEN
});

// create pino logger
const logger = pino(
	{
		browser: {
			transmit: {
				level: 'info',
				send: send
			}
		},
		level: 'debug',
		base: {
			env: process.env.NODE_ENV,
			revision: process.env.VERCEL_GITHUB_COMMIT_SHA
		}
	},
	stream
);

export default logger;
