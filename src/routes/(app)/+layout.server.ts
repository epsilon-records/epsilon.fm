import type { LayoutServerLoad } from './$types';
import { NODE_ENV } from '$env/static/private';

export const load: LayoutServerLoad = async (cookies, url) => {
	console.log(url);
	return {
		nodeEnv: NODE_ENV,
		url: url
	};
};
