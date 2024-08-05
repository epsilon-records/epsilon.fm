import type { PageServerLoad } from './$types.js';
import { getChats } from '$lib/chat';
import _ from 'lodash';

export const load: PageServerLoad = async ({ locals }) => {
	const session = _.get(locals, 'session') as { userId?: string } | undefined;
	const userId = _.get(session, 'userId');
	if (userId) {
		const chats = getChats(userId);
		return {
			chats
		};
	}
};
