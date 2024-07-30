import * as Sentry from '@sentry/sveltekit';
import { sequence } from '@sveltejs/kit/hooks';
import { handleClerk } from 'clerk-sveltekit/server';
import { CLERK_SECRET_KEY } from '$env/static/private';
import type { Handle } from '@sveltejs/kit';

Sentry.init({
	dsn: import.meta.env.SENTRY_DSN,
	tracesSampleRate: 1
});

export const handle: Handle = sequence(
	Sentry.sentryHandle(),
	handleClerk(CLERK_SECRET_KEY, {
		debug: false,
		protectedPaths: [
			'/dashboard',
			'/profile',
			'/profile/account',
			'/profile/appearance',
			'/profile/display',
			'/profile/notifications',
			'/profile/profile',
			'/music',
			'/orders',
			'/products',
			'/customers',
			'/analytics'
		],
		signInUrl: '/sign-in'
	})
);
export const handleError = Sentry.handleErrorWithSentry();
