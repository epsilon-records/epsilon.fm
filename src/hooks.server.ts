import * as Sentry from '@sentry/sveltekit';
import type { Handle } from '@sveltejs/kit';
import { sequence } from '@sveltejs/kit/hooks';
import { handleClerk } from 'clerk-sveltekit/server';
import { SENTRY_DSN, CLERK_SECRET_KEY } from '$env/static/private';
import { redirect } from '@sveltejs/kit';

Sentry.init({
	dsn: SENTRY_DSN,
	tracesSampleRate: 1
});

export const handle: Handle = sequence(
	Sentry.sentryHandle(),
	handleClerk(CLERK_SECRET_KEY, {
		debug: true,
		protectedPaths: [
			'/admin',
			'/profile',
			'/releases',
			'/merch',
			'/website',
			'/social',
			'/royalties'
		],
		signInUrl: '/sign-in'
	}),
	handleSubdomain
);
export const handleError = Sentry.handleErrorWithSentry();

export async function handleSubdomain({ event, resolve }) {
	const { url } = event.request;
	const parsedUrl = new URL(url);
	const subdomain = parsedUrl.hostname.split('.')[0]; // Get the subdomain
	config.log(parsedUrl);
	config.log(subdomain);
	// Define your subdomain to route mappings
	const subdomainRoutes = {
		sub1: '/route1',
		sub2: '/route2'
		// Add more mappings as needed
	};

	if (subdomain in subdomainRoutes) {
		const newUrl = new URL(parsedUrl);
		newUrl.pathname = subdomainRoutes[subdomain];
		config.log(newUrl.toString());
		return redirect(302, newUrl.toString());
	}

	// If no matching subdomain, continue to the requested route
	return await resolve(event);
}
