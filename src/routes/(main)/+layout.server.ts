import type { LayoutServerLoad } from './$types';
import { VERCEL_GIT_COMMIT_SHA } from '$env/static/private';

export const load: LayoutServerLoad = async () => {
	return {
		env: import.meta.env.MODE ?? 'development',
		gitCommitSha: VERCEL_GIT_COMMIT_SHA ?? 'unknown'
	};
};
