import logger from '$lib/logger/logger';
import * as Sentry from '@sentry/sveltekit';
import type { HandleClientError } from '@sveltejs/kit';
import { initializeClerkClient } from 'clerk-sveltekit/client';
import { PUBLIC_CLERK_PUBLISHABLE_KEY } from '$env/static/public';

Sentry.init({
	dsn: 'https://d677a865e0302d7c39f61a919db18993@o337159.ingest.us.sentry.io/4507546312572928',
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
