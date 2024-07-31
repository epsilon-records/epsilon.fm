import { browser } from '$app/environment';
import { QueryClient } from '@tanstack/svelte-query';
import type { LayoutLoad } from './$types';
import { dev } from '$app/environment';
import { inject } from '@vercel/analytics';
import { injectSpeedInsights } from '@vercel/speed-insights/sveltekit';
import posthog from 'posthog-js';
import { env } from '$env/dynamic/public';

inject({ mode: dev ? 'development' : 'production' });
injectSpeedInsights();

export const load: LayoutLoad = (async ({ url }) => {
	const queryClient = new QueryClient({
		defaultOptions: {
			queries: {
				enabled: browser
			}
		}
	});
	if (browser && env.PUBLIC_POSTHOG_API_KEY) {
		posthog.init(env.PUBLIC_POSTHOG_API_KEY, {
			api_host: 'https://eu.i.posthog.com',
			person_profiles: 'identified_only'
		});
	}
	return { url: url, queryClient: queryClient };
}) satisfies LayoutLoad;
