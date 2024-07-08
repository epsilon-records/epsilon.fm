import { dev } from '$app/environment';
import { inject } from '@vercel/analytics';
import { injectSpeedInsights } from '@vercel/speed-insights/sveltekit';
import posthog from 'posthog-js';
import { browser } from '$app/environment';

inject({ mode: dev ? 'development' : 'production' });
injectSpeedInsights();

export const load = async () => {
	if (browser) {
		posthog.init('phc_j5S8Foca22TArMjuKIWR0DhyRt821XV9IqUY1mrOkQJ', {
			api_host: 'https://us.i.posthog.com',
			person_profiles: 'identified_only' // or 'always' to create profiles for anonymous users as well
		});
	}
	return;
};
