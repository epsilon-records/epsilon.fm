<script lang="ts">
	import { Button } from '$lib/components/ui/button';
	import { IconArrowRight } from '$lib/components/ui/icons';
	import type { UseChatHelpers } from 'ai/svelte';

	export let input: UseChatHelpers['input'];

	const exampleMessages = [
		{
			heading: 'Generate album artwork ideas',
			message: `Can you come up with some creative album artwork ideas for my new release?`
		},
		{
			heading: 'Create track titles',
			message: 'Generate some catchy track titles for my upcoming album: \n'
		},
		{
			heading: 'Write lyrics',
			message: `Can you help me write lyrics for a new song I'm working on? \n`
		}
	];
</script>

<div class="mx-auto max-w-2xl px-4">
	<div class="rounded-lg border bg-background p-4">
		<h1 class="mb-2 text-lg font-semibold">🧠 Welcome to the Epsilon AI Music Brain!</h1>
		<p class="leading-normal text-muted-foreground">
			You can start a conversation here or try the following examples:
		</p>
		<div class="mt-4 flex flex-col items-start space-y-2">
			{#each exampleMessages as message}
				<Button
					variant="link"
					class="h-auto p-0 text-base"
					on:click={() => ($input = message.message)}
				>
					<IconArrowRight class="mr-2 text-muted-foreground" />
					{message.heading}
				</Button>
			{/each}
		</div>
	</div>
</div>
