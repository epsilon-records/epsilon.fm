import type { LayoutServerLoad } from './$types';
import { env } from '$env/static/private';

export const load: LayoutServerLoad = async (cookies) => {
	return {
		nodeEnv: env.NODE_ENV
	};
};
