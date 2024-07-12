import type { LayoutServerLoad } from './$types';
import { NODE_ENV, VERCEL_GIT_COMMIT_SHA } from '$env/static/private';

export const load: LayoutServerLoad = async () => {
	return {
		nodeEnv: NODE_ENV,
		gitCommitSha: VERCEL_GIT_COMMIT_SHA
	};
};
