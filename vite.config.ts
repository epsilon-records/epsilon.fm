import { sentrySvelteKit } from '@sentry/sveltekit';
import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vitest/config';
import { enhancedImages } from '@sveltejs/enhanced-img';

export default defineConfig({
	plugins: [
		sentrySvelteKit({
			sourceMapsUploadOptions: {
				org: 'epsilon-records',
				project: 'epsilon'
			}
		}),
		sveltekit(),
		enhancedImages()
	],
	test: {
		include: ['src/**/*.{test,spec}.{js,ts}']
	},
	define: {
		'process.env.NODE_ENV': JSON.stringify(process.env.NODE_ENV),
		'process.env.VERCEL_GITHUB_COMMIT_SHA': JSON.stringify(process.env.VERCEL_GITHUB_COMMIT_SHA),
		'import.meta.env.MODE': JSON.stringify(process.env.NODE_ENV),
		'import.meta.env.VERCEL_GITHUB_COMMIT_SHA': JSON.stringify(process.env.VERCEL_GITHUB_COMMIT_SHA)
	}
});
