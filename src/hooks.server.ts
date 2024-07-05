import * as Sentry from '@sentry/sveltekit';
import type { Handle } from '@sveltejs/kit';
import { sequence } from '@sveltejs/kit/hooks';
import { handleClerk } from 'clerk-sveltekit/server';
import { CLERK_SECRET_KEY } from '$env/static/private';

Sentry.init({
    dsn: "https://d677a865e0302d7c39f61a919db18993@o337159.ingest.us.sentry.io/4507546312572928",
    tracesSampleRate: 1
})

export const handle: Handle = sequence(Sentry.sentryHandle(), sequence(
	handleClerk(CLERK_SECRET_KEY, {
		debug: true,
		protectedPaths: [
			'/admin',
			'/profile',
			'releases',
			'merch',
			'website',
			'social',
			'royalties',
			'admin'
		],
		signInUrl: '/sign-in'
	})
));
export const handleError = Sentry.handleErrorWithSentry();