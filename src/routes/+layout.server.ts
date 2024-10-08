import type { LayoutServerLoad } from './$types';
import { env } from '$env/dynamic/private';

export const load: LayoutServerLoad = async () => {
	return {
		env: env.MODE ?? 'development',
		gitCommitSha: env.VERCEL_GIT_COMMIT_SHA ?? 'unknown'
	};
};
