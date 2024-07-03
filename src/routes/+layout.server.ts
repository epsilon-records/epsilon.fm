import type { LayoutServerLoad } from './$types';
import { NODE_ENV } from '$env/static/private';

export const load: LayoutServerLoad = async (event) => {
	const session = await event.locals.auth();

	return {
		session,
		nodeEnv: NODE_ENV
	};
};
