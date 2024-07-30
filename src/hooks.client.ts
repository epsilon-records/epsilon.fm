//import logger from '$lib/logger';
import * as Sentry from '@sentry/sveltekit';
import type { HandleClientError } from '@sveltejs/kit';
import { initializeClerkClient } from 'clerk-sveltekit/client';
import { env } from '$env/dynamic/public';

Sentry.init({
	dsn: import.meta.env.SENTRY_DSN,
	tracesSampleRate: 1,
	replaysSessionSampleRate: 0.1,
	replaysOnErrorSampleRate: 1,
	integrations: [Sentry.replayIntegration()]
});

initializeClerkClient(env.PUBLIC_CLERK_PUBLISHABLE_KEY, {
	afterSignInUrl: '/dashboard',
	afterSignUpUrl: '/dashboard',
	signInUrl: '/sign-in',
	signUpUrl: '/sign-up'
});

export const handleError: HandleClientError = ({ error, event }) => {
	console.error('An error occurred on the client side:', error, event);
};
