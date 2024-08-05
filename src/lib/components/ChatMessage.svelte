<script lang="ts">
	import ChatMessageActions from '$lib/components/ChatMessageActions.svelte';
	import type { Message } from 'ai';
	import Typewriter from 'svelte-typewriter';
	export let message: Message;
	export let typewriter: boolean;

	let timestamp = '';
	if (message.createdAt) {
		timestamp = new Date(message.createdAt).toLocaleTimeString();
	}
</script>

<div class="w-full">
	{#if message.role === 'assistant'}
		<div class="chat chat-start">
			<div class="avatar chat-image">
				<div class="w-10 rounded-full text-4xl">🧠</div>
			</div>
			<div class="chat-header">
				Epsilon Brain
				<time class="text-xs opacity-50">{timestamp}</time>
			</div>
			<div class="chat-bubble">
				{#if typewriter}
					<Typewriter interval={50} loop={false} cursor={true}>
						{message.content}
					</Typewriter>
				{:else}
					{message.content}
				{/if}
			</div>
			<div class="chat-footer opacity-50">Delivered</div>
		</div>
	{:else}
		<div class="chat chat-end">
			<div class="chat-header text-right">
				Anakin
				<time class="text-xs opacity-50">{timestamp}</time>
			</div>
			<div class="chat-bubble">{message.content}</div>

			<div class="chat-footer text-right opacity-50">Seen at {timestamp}</div>

			<div class="avatar chat-image">
				<div class="w-10 rounded-full text-4xl">🧙</div>
			</div>
		</div>
	{/if}
	<ChatMessageActions {message} />
</div>
