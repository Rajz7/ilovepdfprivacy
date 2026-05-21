import React from 'react';
import { Link } from 'react-router-dom';

const TOOL_BADGES = {
  'Merge PDF': 'Combine',
  'Split PDF': 'Extract',
  'Compress PDF': 'Optimize',
  'Word to PDF': 'Convert',
  'Powerpoint to PDF': 'Convert',
  'Image to PDF': 'Compose',
};

const ToolCard = ({ title, description, path, index = 0 }) => {
  return (
    <Link
      to={path}
      className="appear-up group relative overflow-hidden rounded-2xl border border-slate-200/80 bg-white/80 p-6 shadow-[0_18px_40px_-28px_rgba(15,23,42,0.75)] backdrop-blur-xl transition-all duration-300 hover:-translate-y-1 hover:border-teal-300 hover:shadow-[0_28px_50px_-30px_rgba(13,148,136,0.65)]"
      style={{ animationDelay: `${280 + index * 70}ms` }}
    >
      <span className="mb-4 inline-flex items-center rounded-full border border-slate-200 bg-white px-2.5 py-1 text-[11px] font-semibold uppercase tracking-[0.18em] text-slate-500">
        {TOOL_BADGES[title] || 'Tool'}
      </span>

      <h3 className="font-display text-2xl font-semibold tracking-tight text-slate-900">
        {title}
      </h3>

      <p className="mt-3 text-sm leading-relaxed text-slate-600">
        {description}
      </p>

      <div className="mt-6 inline-flex items-center text-sm font-semibold text-teal-700 transition-all duration-300 group-hover:translate-x-1">
        Open tool
        <span className="ml-2">→</span>
      </div>

      <div className="pointer-events-none absolute -right-12 -top-12 h-28 w-28 rounded-full bg-gradient-to-br from-cyan-200/50 via-emerald-100/30 to-transparent" />
    </Link>
  );
};

export default ToolCard;
