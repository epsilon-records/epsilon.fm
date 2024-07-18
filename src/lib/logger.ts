import pino from 'pino';
import { logflarePinoVercel } from 'pino-logflare';
import { PUBLIC_LOGFLARE_API_KEY, PUBLIC_LOGFLARE_SOURCE_TOKEN } from '$env/static/public';

// Browser logs are going to: https://logflare.app/sources/32475
// Server logs are going to: https://logflare.app/sources/32465

const { stream, send } = logflarePinoVercel({
	apiKey: PUBLIC_LOGFLARE_API_KEY,
	sourceToken: PUBLIC_LOGFLARE_SOURCE_TOKEN
});

const isBrowser = typeof window !== 'undefined';

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
			env: isBrowser ? import.meta.env.MODE : process.env.NODE_ENV,
			revision: isBrowser
				? import.meta.env.VITE_VERCEL_GITHUB_COMMIT_SHA
				: process.env.VERCEL_GITHUB_COMMIT_SHA
		}
	},
	stream
);

export default logger;
