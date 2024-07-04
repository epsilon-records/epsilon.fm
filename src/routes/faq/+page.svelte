<script lang="ts">
	import * as Card from '$lib/components/ui/card';
	import * as Accordion from '$lib/components/ui/accordion';
</script>

<Card.Root class="m-4">
	<Card.Header>
		<Card.Title>FAQ</Card.Title>
		<Card.Description>Frequently Asked Questions ❓</Card.Description>
	</Card.Header>
	<Card.Content>
		<Accordion.Root class="w-full self-center sm:max-w-[100%]">
			<Accordion.Item value="item-1">
				<Accordion.Trigger>Is it accessible?</Accordion.Trigger>
				<Accordion.Content>Yes. It adheres to the WAI-ARIA design pattern.</Accordion.Content>
			</Accordion.Item>
			<Accordion.Item value="item-2">
				<Accordion.Trigger>Is it styled?</Accordion.Trigger>
				<Accordion.Content>
					Yes. It comes with default styles that matches the other components' aesthetic.
				</Accordion.Content>
			</Accordion.Item>
			<Accordion.Item value="item-3">
				<Accordion.Trigger>Is it animated?</Accordion.Trigger>
				<Accordion.Content>
					Yes. It's animated by default, but you can disable it if you prefer.
				</Accordion.Content>
			</Accordion.Item>
		</Accordion.Root>
	</Card.Content>
</Card.Root>
