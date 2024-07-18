import logger from '$lib/logger/logger';
import * as Sentry from '@sentry/sveltekit';
import type { HandleClientError } from '@sveltejs/kit';
import { initializeClerkClient } from 'clerk-sveltekit/client';
import { SENTRY_DSN } from '$env/dynamic/public';
import { PUBLIC_CLERK_PUBLISHABLE_KEY } from '$env/static/public';

Sentry.init({
	dsn: SENTRY_DSN,
	tracesSampleRate: 1,
	replaysSessionSampleRate: 0.1,
	replaysOnErrorSampleRate: 1,
	integrations: [Sentry.replayIntegration()]
});

initializeClerkClient(PUBLIC_CLERK_PUBLISHABLE_KEY, {
	afterSignInUrl: '/',
	afterSignUpUrl: '/',
	signInUrl: '/sign-in',
	signUpUrl: '/sign-up'
});

export const handleError: HandleClientError = Sentry.handleErrorWithSentry(
	async ({ error, event }) => {
		if (error instanceof Error) {
			logger.error(error.message, { error, event });
		} else {
			logger.error('An unknown error occurred', { error, event });
		}
	}
);
