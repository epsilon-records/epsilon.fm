import pino from 'pino';
import { logflarePinoVercel } from 'pino-logflare';
import { PUBLIC_LOGFLARE_API_KEY, PUBLIC_LOGFLARE_SOURCE_TOKEN } from '$env/static/public';

// Browser logs are draining to https://logflare.app/sources/32475
// Server logs are draining to https://logflare.app/sources/32465

const { stream, send } = logflarePinoVercel({
	apiKey: PUBLIC_LOGFLARE_API_KEY,
	sourceToken: PUBLIC_LOGFLARE_SOURCE_TOKEN
});

const isBrowser = typeof window !== 'undefined';

// Safe access to environment variables
const env = isBrowser
	? import.meta.env.MODE || 'development'
	: process.env.NODE_ENV || 'development';
const revision = isBrowser
	? import.meta.env.VITE_VERCEL_GITHUB_COMMIT_SHA || 'unknown'
	: process.env.VERCEL_GITHUB_COMMIT_SHA || 'unknown';

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
			env: env,
			revision: revision
		}
	},
	stream
);

export default logger;
