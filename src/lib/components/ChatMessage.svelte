<script lang="ts">
	import ChatMessageActions from '$lib/components/ChatMessageActions.svelte';
	import { IconOpenAI, IconUser } from '$lib/components/ui/icons';
	import SpinningLogo from '@/components/SpinningLogo.svelte';
	import { cn } from '$lib/utils';
	import type { Message } from 'ai';
	import Typewriter from 'svelte-typewriter';
	export let message: Message;
	export let typewriter: boolean;
</script>

<div class={cn('group relative mb-4 flex items-start md:-ml-12')} {...$$restProps}>
	<div
		class={cn(
			'flex h-8 w-8 shrink-0 select-none items-center justify-center rounded-md border shadow',
			message.role === 'user' ? 'bg-background' : 'bg-primary text-primary-foreground'
		)}
	>
		{#if message.role === 'user'}
			<IconUser />
		{:else}
			🧠
		{/if}
	</div>
	<div class="ml-4 mt-1 w-screen flex-1 overflow-hidden px-1">
		{#if typewriter && message.role === 'assistant'}
			<Typewriter speed={50} delay={100} loop={true} cursor={true}>
				{message.content}
			</Typewriter>
		{:else}
			{message.content}
		{/if}
	</div>
	<ChatMessageActions {message} />
</div>
