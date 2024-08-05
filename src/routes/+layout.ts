import { browser } from '$app/environment';
import { QueryClient } from '@tanstack/svelte-query';
import type { LayoutLoad } from './$types';
import { dev } from '$app/environment';
import { inject } from '@vercel/analytics';
import posthog from 'posthog-js';
import { env } from '$env/dynamic/public';
import { client as soundchartsClient } from '$lib/api/soundcharts/client';

inject({ mode: dev ? 'development' : 'production' });

export const load: LayoutLoad = (async ({ url }) => {
	const queryClient = new QueryClient({
		defaultOptions: {
			queries: {
				enabled: browser
			}
		}
	});

	// soundchartsClient.setConfig({
	// 	baseUrl: 'https://customer.api.soundcharts.com'
	// });

	// soundchartsClient.interceptors.request.use((request, options) => {
	// 	request.headers.set('x-api-key', SOUNDCHARTS_API_KEY);
	// 	request.headers.set('x-app-id', SOUNDCHARTS_APP_ID);
	// 	return request;
	// });

	if (browser && env.PUBLIC_POSTHOG_API_KEY) {
		posthog.init(env.PUBLIC_POSTHOG_API_KEY, {
			api_host: 'https://eu.i.posthog.com',
			person_profiles: 'identified_only'
		});
	}
	return { url: url, queryClient: queryClient, soundchartsClient: soundchartsClient };
}) satisfies LayoutLoad;
