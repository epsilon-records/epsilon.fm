import type { LayoutServerLoad } from './$types';
import { NODE_ENV } from '$env/static/private';

export const load: LayoutServerLoad = async () => {
	return {
		nodeEnv: NODE_ENV
	};
};
