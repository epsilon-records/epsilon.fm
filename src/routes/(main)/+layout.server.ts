import type { LayoutServerLoad } from './$types';
import { PUBLIC_VERCEL_ENV } from '$env/static/public';
import { VERCEL_GIT_COMMIT_SHA } from '$env/static/private';

export const load: LayoutServerLoad = async () => {
	return {
		nodeEnv: PUBLIC_VERCEL_ENV,
		gitCommitSha: VERCEL_GIT_COMMIT_SHA
	};
};
