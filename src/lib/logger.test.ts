import { describe, it, expect, vi, beforeEach, afterEach } from 'vitest';
import logger from './logger';
import type { MockInstance } from 'vitest';

describe('Logger Tests', () => {
	let consoleErrorSpy: MockInstance;
	let consoleWarnSpy: MockInstance;
	let consoleInfoSpy: MockInstance;
	let consoleDebugSpy: MockInstance;

	beforeEach(() => {
		consoleErrorSpy = vi.spyOn(console, 'error').mockImplementation(() => undefined);
		consoleWarnSpy = vi.spyOn(console, 'warn').mockImplementation(() => undefined);
		consoleInfoSpy = vi.spyOn(console, 'info').mockImplementation(() => undefined);
		consoleDebugSpy = vi.spyOn(console, 'debug').mockImplementation(() => undefined);

		vi.resetModules();
		vi.mock('pino', () => {
			return {
				default: vi.fn(() => ({
					error: vi.fn((msg) => console.error(JSON.stringify({ level: 50, msg }))),
					warn: vi.fn((msg) => console.warn(JSON.stringify({ level: 40, msg }))),
					info: vi.fn((msg) => console.info(JSON.stringify({ level: 30, msg }))),
					debug: vi.fn((msg) => console.debug(JSON.stringify({ level: 20, msg }))),
					trace: vi.fn((msg) => console.debug(JSON.stringify({ level: 10, msg })))
				}))
			};
		});
	});

	afterEach(() => {
		vi.clearAllMocks();
	});

	it('should be an instance of pino logger', () => {
		expect(logger).toBeDefined();
		expect(typeof logger.info).toBe('function');
		expect(typeof logger.error).toBe('function');
		expect(typeof logger.debug).toBe('function');
		expect(typeof logger.warn).toBe('function');
	});

	it('should log error messages', () => {
		logger.error('This is an error message');
		expect(consoleErrorSpy).toHaveBeenCalled();
		const loggedMessage = JSON.parse(consoleErrorSpy.mock.calls[0][0] as string);
		expect(loggedMessage.level).toBe(50); // 50 is the level for 'error'
		expect(loggedMessage.msg).toBe('This is an error message');
	});

	it('should log warn messages', () => {
		logger.warn('This is a warning message');
		expect(consoleWarnSpy).toHaveBeenCalled();
		const loggedMessage = JSON.parse(consoleWarnSpy.mock.calls[0][0] as string);
		expect(loggedMessage.level).toBe(40); // 40 is the level for 'warn'
		expect(loggedMessage.msg).toBe('This is a warning message');
	});

	it('should log info messages', () => {
		logger.info('This is an info message');
		expect(consoleInfoSpy).toHaveBeenCalled();
		const loggedMessage = JSON.parse(consoleInfoSpy.mock.calls[0][0] as string);
		expect(loggedMessage.level).toBe(30); // 30 is the level for 'info'
		expect(loggedMessage.msg).toBe('This is an info message');
	});

	it('should log debug messages', () => {
		logger.debug('This is a debug message');
		expect(consoleDebugSpy).toHaveBeenCalled();
		const loggedMessage = JSON.parse(consoleDebugSpy.mock.calls[0][0] as string);
		expect(loggedMessage.level).toBe(20); // 20 is the level for 'debug'
		expect(loggedMessage.msg).toBe('This is a debug message');
	});
});
