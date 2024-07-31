import type { PageServerLoad } from './$types.js';
import { userId } from '$lib/stores/auth';

export const load: PageServerLoad = async ({ locals }) => {
	const session = (locals as { session?: { user?: { id?: string } } }).session;
	if (session && session.user && session.user.id) {
		console.log(session.user.id);
		userId.set(session.user.id);
	}
};
