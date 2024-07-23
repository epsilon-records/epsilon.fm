//import logger from '$lib/logger';
import * as Sentry from '@sentry/sveltekit';
import type { HandleClientError } from '@sveltejs/kit';
import { initializeClerkClient } from 'clerk-sveltekit/client';
import { PUBLIC_CLERK_PUBLISHABLE_KEY } from '$env/static/public';

Sentry.init({
	dsn: import.meta.env.SENTRY_DSN,
	tracesSampleRate: 1,
	replaysSessionSampleRate: 0.1,
	replaysOnErrorSampleRate: 1,
	integrations: [Sentry.replayIntegration()]
});

initializeClerkClient(PUBLIC_CLERK_PUBLISHABLE_KEY, {
	afterSignInUrl: '/music',
	afterSignUpUrl: '/music',
	signInUrl: '/sign-in',
	signUpUrl: '/sign-up'
});

export const handleError: HandleClientError = ({ error, event }) => {
	console.error('An error occurred on the client side:', error, event);
};
