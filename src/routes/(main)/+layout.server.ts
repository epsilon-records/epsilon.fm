import type { LayoutServerLoad } from './$types';

export const load: LayoutServerLoad = async () => {
	return {
		env: import.meta.env.MODE ?? 'development',
		gitCommitSha: import.meta.env.VERCEL_GIT_COMMIT_SHA ?? 'unknown'
	};
};
