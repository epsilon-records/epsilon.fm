<script lang="ts">
	import { page } from '$app/stores';
	import { Section, Page404, Page500 } from 'flowbite-svelte-blocks';
	import { Button } from 'flowbite-svelte';
</script>

{#if $page.status === 404}
	<Section name="page404">
		<Page404>
			<svelte:fragment slot="h1">404</svelte:fragment>
			<svelte:fragment slot="paragraph">
				<p class="mb-4 text-3xl font-bold tracking-tight text-gray-900 dark:text-white md:text-4xl">
					Something's missing.
				</p>
				<p class="mb-4 text-lg font-light text-gray-500 dark:text-gray-400">
					Sorry, we can't find that page. You'll find lots to explore on the home page.
				</p>
				<Button href="/" size="lg" color="red">Back to Homepage</Button>
			</svelte:fragment>
		</Page404>
	</Section>
{:else}
	<Section name="page500">
		<Page500>
			<svelte:fragment slot="h1">500</svelte:fragment>
			<svelte:fragment slot="paragraph">
				<p class="mb-4 text-3xl font-bold tracking-tight text-gray-900 dark:text-white md:text-4xl">
					Internal Server Error.
				</p>
				<p class="mb-4 text-lg font-light text-gray-500 dark:text-gray-400">
					We are already working to solve the problem.
				</p>
			</svelte:fragment>
		</Page500>
	</Section>
{/if}
