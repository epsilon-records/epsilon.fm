import { error, redirect } from '@sveltejs/kit';
import type { PageServerLoad } from './$types';
import { getChat } from '$lib/chat';
import _ from 'lodash';
import { currentUserId } from '$lib/stores/brain';

export const load: PageServerLoad = async ({ params, locals }) => {
	// Use type assertion to access 'session'
	const session = _.get(locals, 'session') as { userId?: string } | undefined;
	const userId = _.get(session, 'userId');
	if (userId) {
		currentUserId.set(userId);
	} else {
		throw redirect(302, `/sign-in?redirect=/brain/chat/${params.id}`);
	}
	const chat = await getChat(params.id, userId);
	if (!chat) {
		throw error(404, 'Not found');
	}
	return { chat };
};
