<script lang="ts">
	import ChatMessage from '$lib/components/ChatMessage.svelte';
	import { Separator } from '$lib/components/ui/separator';
	import type { UseChatHelpers } from 'ai/svelte';

	export let messages: UseChatHelpers['messages'];
</script>

{#if $messages?.length}
	<div class="relative mx-auto w-[48rem] max-w-2xl px-4">
		{#each $messages as message, index}
			{#if index == $messages.length - 1}
				<ChatMessage {message} typewriter={true} />
			{:else}
				<ChatMessage {message} typewriter={false} />
			{/if}
		{/each}
	</div>
{/if}
