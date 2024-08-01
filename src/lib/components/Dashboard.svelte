<script lang="ts">
	import SignedIn from 'clerk-sveltekit/client/SignedIn.svelte';
</script>

<main
	class="grid h-min flex-1 items-start gap-4 p-4 sm:px-6 sm:py-0 md:gap-8 lg:grid-cols-3 xl:grid-cols-3"
>
	<SignedIn>
		<div class="grid auto-rows-max items-start justify-center gap-4 pb-16 md:gap-8 lg:col-span-2">
			<div class="grid gap-8 sm:grid-cols-2 md:grid-cols-4 lg:grid-cols-2 xl:grid-cols-4">
				<div class="min-w-[20rem]">
					<slot name="topLeft" />
				</div>
				<slot name="topCenter" />
				<slot name="topRight" />
			</div>
			<div class="grid gap-8 sm:grid-cols-2 md:grid-cols-4 lg:grid-cols-2 xl:grid-cols-4">
				<slot name="content" />
			</div>
		</div>
		<slot name="sidebar" />
	</SignedIn>
</main>
