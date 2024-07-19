import pino from 'pino';
import { logflarePinoVercel } from 'pino-logflare';
import { PUBLIC_LOGFLARE_API_KEY, PUBLIC_LOGFLARE_SOURCE_TOKEN } from '$env/static/public';

// Browser logs are draining to https://logflare.app/sources/32475
// Server logs are draining to https://logflare.app/sources/32465

const { stream, send } = logflarePinoVercel({
	apiKey: PUBLIC_LOGFLARE_API_KEY,
	sourceToken: PUBLIC_LOGFLARE_SOURCE_TOKEN
});

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
			env: import.meta.env.VERCEL_ENV,
			revision: import.meta.env.VERCEL_GIT_COMMIT_SHA
		}
	},
	stream
);

export default logger;
