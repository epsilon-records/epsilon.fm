import type { LayoutServerLoad } from './$types';
import { VERCEL_GIT_COMMIT_SHA } from '$env/static/private';
import { PUBLIC_MODE } from '$env/static/public';

export const load: LayoutServerLoad = async () => {
	return {
		env: PUBLIC_MODE,
		gitCommitSha: VERCEL_GIT_COMMIT_SHA
	};
};
