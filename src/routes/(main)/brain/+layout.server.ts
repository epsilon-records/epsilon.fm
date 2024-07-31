import { getChats } from '$lib/chat';
import type { LayoutServerLoad } from './$types';
import { userId } from '$lib/stores/auth';

export const load: LayoutServerLoad = async () => {
	const chats = getChats(`${userId}`);
	return {
		chats
	};
};
