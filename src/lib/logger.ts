import pino from 'pino';
import { logflarePinoVercel } from 'pino-logflare';

// Browser logs are going to: https://logflare.app/sources/32475
// Server logs are going to: https://logflare.app/sources/32465

const { stream, send } = logflarePinoVercel({
	apiKey: import.meta.env.LOGFLARE_API_KEY!,
	sourceToken: import.meta.env.LOGFLARE_SOURCE_TOKEN!
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
