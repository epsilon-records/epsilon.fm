import vercelAdapter from '@sveltejs/adapter-vercel';
import nodeAdapter from '@sveltejs/adapter-node';
import autoAdapter from '@sveltejs/adapter-auto';
import { vitePreprocess } from '@sveltejs/vite-plugin-svelte';

/** @type {import('@sveltejs/kit').Config} */
const config = {
	preprocess: [vitePreprocess()],
	kit: {
		adapter: getAdapter(),
		csrf: {
			checkOrigin: true
		},
		alias: {
			'@/*': './src/lib/*',
			'$src/*': './src/*'
		}
	}
};

function getAdapter() {
	if (process.env.VERCEL && process.env.MODE === 'production') {
		return vercelAdapter({
			runtime: 'edge',
			regions: 'fra1',
			split: true,
			images: {
				sizes: [640, 828, 1200, 1920, 3840],
				formats: ['image/avif', 'image/webp'],
				minimumCacheTTL: 300,
				domains: [process.env.BASE_URL]
			}
		});
	} else if (process.env.RAILWAY && process.env.MODE === 'production') {
		return nodeAdapter();
	} else {
		return autoAdapter();
	}
}

export default config;
