<script lang="ts">
	import ChatMessage from '$lib/components/ChatMessage.svelte';
	import { Separator } from '$lib/components/ui/separator';
	import type { UseChatHelpers } from 'ai/svelte';

	export let messages: UseChatHelpers['messages'];
</script>

{#if $messages?.length}
	<div class="relative mx-auto max-w-2xl px-4">
		{#each $messages as message, index}
			<div>
				<ChatMessage {message} />
				{#if index < $messages.length - 1}
					<Separator class="md:my-2" />
				{/if}
			</div>
		{/each}
	</div>
{/if}
