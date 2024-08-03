<script lang="ts">
	import { page } from '$app/stores';
	import { Section, Page404, Page500 } from 'flowbite-svelte-blocks';
	import { Button } from '$lib/components/ui/button';
</script>

<div class="flex items-center justify-center">
	{#if $page.status === 404}
		<Section name="page404">
			<Page404>
				<svelte:fragment slot="h1"><div class="text-4xl">404</div></svelte:fragment>
				<svelte:fragment slot="paragraph">
					<p
						class="mb-4 text-3xl font-bold tracking-tight text-gray-900 dark:text-white md:text-4xl"
					>
						Oops! Page not found.
					</p>
					<p class="mb-4 text-lg font-light text-gray-500 dark:text-gray-400">
						The page you're looking for doesn't exist or has been moved. Let's get you back on
						track.
					</p>
					<Button href="/" size="lg">🏠 Return Home</Button>
				</svelte:fragment>
			</Page404>
		</Section>
	{:else}
		<Section name="page500">
			<Page500>
				<svelte:fragment slot="h1"><div class="text-4xl">500</div></svelte:fragment>
				<svelte:fragment slot="paragraph">
					<p
						class="mb-4 text-3xl font-bold tracking-tight text-gray-900 dark:text-white md:text-4xl"
					>
						Oops! Something went wrong.
					</p>
					<p class="mb-4 text-lg font-light text-gray-500 dark:text-gray-400">
						We're experiencing some technical difficulties. Our team has been notified and is
						working on a fix.
					</p>
					<Button href="/dashboard" size="lg">🔄 Try Again</Button>
				</svelte:fragment>
			</Page500>
		</Section>
	{/if}
</div>
