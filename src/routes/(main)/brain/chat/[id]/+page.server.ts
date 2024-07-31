import { error, redirect } from '@sveltejs/kit';
import type { PageServerLoad } from './$types';
import { getChat } from '$lib/chat';
import { userId } from '$lib/stores/auth';

export const load: PageServerLoad = async ({ params }) => {
	if (!userId) {
		throw redirect(302, `/sign-in?redirect=/brain/chat/${params.id}`);
	}
	const chat = await getChat(params.id, `${userId}`);
	if (!chat) {
		throw error(404, 'Not found');
	}
	return { chat };
};
