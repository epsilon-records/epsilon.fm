import * as Sentry from '@sentry/sveltekit';
import type { Handle } from '@sveltejs/kit';
import { sequence } from '@sveltejs/kit/hooks';
import { handleClerk } from 'clerk-sveltekit/server';
import { env } from '$env/static/private';
import { redirect } from '@sveltejs/kit';

Sentry.init({
	dsn: env.SENTRY_DSN,
	tracesSampleRate: 1
});

export const handle: Handle = sequence(
	Sentry.sentryHandle(),
	handleClerk(env.CLERK_SECRET_KEY, {
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
	handleSubdomain(event, resolve)
);
export const handleError = Sentry.handleErrorWithSentry();

export async function handleSubdomain({ event, resolve }) {
	const { url } = event.request;
	const parsedUrl = new URL(url);
	const subdomain = parsedUrl.hostname.split('.')[0]; // Get the subdomain

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
