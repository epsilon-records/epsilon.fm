import * as Sentry from '@sentry/sveltekit';
import { sequence } from '@sveltejs/kit/hooks';
import { handleClerk } from 'clerk-sveltekit/server';
import { CLERK_SECRET_KEY } from '$env/static/private';
import { redirect } from '@sveltejs/kit';
import type { Handle } from '@sveltejs/kit';

type SubdomainRoutes = {
	[key: string]: string;
};

Sentry.init({
	dsn: process.env.SENTRY_DSN,
	tracesSampleRate: 1
});

export const handleSubdomain: Handle = async ({ event, resolve }) => {
	const { url } = event.request;
	const parsedUrl = new URL(url);
	const subdomain = parsedUrl.hostname.split('.')[0]; // Get the subdomain
	// Define your subdomain to route mappings
	const subdomainRoutes: SubdomainRoutes = {
		sub1: '/route1',
		sub2: '/route2'
		// Add more mappings as needed
	};

	if (subdomain in subdomainRoutes) {
		const newUrl = new URL(parsedUrl);
		newUrl.pathname = subdomainRoutes[subdomain as keyof SubdomainRoutes];
		return redirect(302, newUrl.toString());
	}

	// If no matching subdomain, continue to the requested route
	return await resolve(event);
};

export const handle: Handle = sequence(
	Sentry.sentryHandle(),
	handleClerk(CLERK_SECRET_KEY, {
		debug: false,
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
