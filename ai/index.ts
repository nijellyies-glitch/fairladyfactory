import { config } from 'dotenv';
import { generateText, gateway } from 'ai';

// Load the local key from .env.local (gitignored — never committed)
config({ path: '.env.local' });

// Note: openai/gpt-5.5 requires paid AI Gateway credits; the free tier
// restricts some models. Default here is a free-tier model.
// Override with GATEWAY_MODEL env var, e.g. GATEWAY_MODEL=openai/gpt-5.5
const modelId = process.env.GATEWAY_MODEL || 'openai/gpt-4o-mini';

const result = await generateText({
  model: gateway(modelId),
  prompt: 'Invent a new holiday and describe its traditions.',
});

console.log(result.text);
