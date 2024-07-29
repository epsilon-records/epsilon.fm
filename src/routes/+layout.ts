import { browser } from '$app/environment';
import { QueryClient } from '@tanstack/svelte-query';
import type { LayoutLoad } from './$types';
import { dev } from '$app/environment';
import { inject } from '@vercel/analytics';
import { injectSpeedInsights } from '@vercel/speed-insights/sveltekit';
import posthog from 'posthog-js';
import { env } from '$env/dynamic/public';

// export const prerender = true;
// export const ssr = false;

inject({ mode: dev ? 'development' : 'production' });
injectSpeedInsights();

export const load: LayoutLoad = (async () => {
	const queryClient = new QueryClient({
		defaultOptions: {
			queries: {
				enabled: browser
				// staleTime: 60 * 1000
			}
		}
	});
	if (browser && env.PUBLIC_POSTHOG_API_KEY) {
		posthog.init(env.PUBLIC_POSTHOG_API_KEY, {
			api_host: 'https://eu.i.posthog.com',
			person_profiles: 'identified_only' // or 'always' to create profiles for anonymous users as well
		});
	}
	return { queryClient };
}) satisfies LayoutLoad;
