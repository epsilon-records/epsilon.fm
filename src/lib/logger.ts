import pino from 'pino';
import { logflarePinoVercel } from 'pino-logflare';
import { PUBLIC_LOGFLARE_API_KEY, PUBLIC_LOGFLARE_SOURCE_TOKEN } from '$env/static/public';

// Browser logs are going to: https://logflare.app/sources/32475
// Server logs are going to: https://logflare.app/sources/32465

const { stream, send } = logflarePinoVercel({
	apiKey: PUBLIC_LOGFLARE_API_KEY,
	sourceToken: PUBLIC_LOGFLARE_SOURCE_TOKEN
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
			env: import.meta.env.NODE_ENV,
			revision: import.meta.env.VERCEL_GITHUB_COMMIT_SHA
		}
	},
	stream
);

export default logger;
